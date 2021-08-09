#!/usr/bin/env python3

import pygame
import sys
import random
import numpy as np
from collections import deque
import cv2

#import tensorflow as tf #这是2.0，得用v1，并把v2关掉。。。
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_SIZE = (320, 400)
BAR_SIZE = (40, 5)
BALL_SIZE = (15, 15)

#神经网络的输出
MOVE_STAY = [1, 0, 0]
MOVE_LEFT = [0, 1, 0]
MOVE_RIGHT = [0, 0, 1]

class Game(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption('game2withAi')

        self.ball_pos_x = SCREEN_SIZE[0] // 2 - BALL_SIZE[0] / 2 #x居中
        self.ball_pos_y = SCREEN_SIZE[1] // 2 - BALL_SIZE[1] / 2 #y居中

        #Ball移动方向
        self.ball_dir_x = -1 #left
        self.ball_dir_y = -1 #up #来回换方向的
        self.ball_pos = pygame.Rect(self.ball_pos_x, self.ball_pos_y, BALL_SIZE[0], BALL_SIZE[1])
        #Rect(left, top, width, height) -> Rect

        self.score = 0
        self.bar_pos_x = SCREEN_SIZE[0] // 2 - BAR_SIZE[0] // 2 #x居中
        self.bar_pos_y = SCREEN_SIZE[1] - BAR_SIZE[1] #y在底部
        self.bar_pos = pygame.Rect(self.bar_pos_x, self.bar_pos_y, BAR_SIZE[0], BAR_SIZE[1])

    def bar_move_left(self):
        self.bar_pos_x -= 2
        if self.bar_pos_x <= 0:
            self.bar_pos_x = 0
    def bar_move_right(self):
        self.bar_pos_x += 2
        if self.bar_pos_x > SCREEN_SIZE[0] - BAR_SIZE[0]:
            self.bar_pos_x = SCREEN_SIZE[0] - BAR_SIZE[0]
    
    #action 是MOVE, 停或左右
    #AI控制BAR左右移动，返回游戏界面像素和对应的奖励
    #像素->奖励->强化BAR往奖励高的方向移动
    def step(self, action):
        if action == MOVE_LEFT:
            self.bar_move_left()
        elif action == MOVE_RIGHT:
            self.bar_move_right()

        self.screen.fill(BLACK)
        self.bar_pos.left = self.bar_pos_x
        pygame.draw.rect(self.screen, WHITE, self.bar_pos)

        self.ball_pos.left += self.ball_dir_x * 3
        self.ball_pos.bottom += self.ball_dir_y * 5
        pygame.draw.rect(self.screen, WHITE, self.ball_pos)

        if self.ball_pos.top <= 0 or self.ball_pos.bottom >= (SCREEN_SIZE[1] - BAR_SIZE[1]+1): #不多向下走1可能永远接不到，因为下面是判断走到了或<1的，还是算碰撞好
            self.ball_dir_y = self.ball_dir_y * -1 #碰到上返回，下附近就返回
        if self.ball_pos.left <= 0 or self.ball_pos.right >= (SCREEN_SIZE[0]):
            self.ball_dir_x = self.ball_dir_x * -1 #碰到左右返回

        reward = 0
        if self.bar_pos.top <= self.ball_pos.bottom and (self.bar_pos.left < self.ball_pos.right and self.bar_pos.right > self.ball_pos.left):
            reward = 1 #手动判断接住，左边缘，并且，右边缘，之内，先球好判断
        if self.bar_pos.top <= self.ball_pos.bottom and (self.bar_pos.left > self.ball_pos.right or self.bar_pos.right < self.ball_pos.left):
            reward = -1 #手动判断没接住

        #获得游戏界面像素
        screen_image = pygame.surfarray.array3d(pygame.display.get_surface())
        pygame.display.update()
        #self.clock.tick(60) #电脑自己玩，就能多快就多快了
        return reward, screen_image #返回这个和奖励来调整下一次输入的action

#不知道为什么这样设置。下次继续调用得了
LEARNING_RATE = 0.99

#更新梯度#不明白意思
INITIAL_EPSILON = 1.0
FINAL_EPSILON = 0.05

#测试观测次数
EXPLORE = 500000
OBSERVE = 50000

#存储过往经验大小
REPLAY_MEMORY = 500000

BATCH = 100 #批量100个样品

output = 3 #输出层神经元数，3种操作
input_image = tf.placeholder("float", [None, 80, 100, 4]) #？个图
#batch, height, width, channels. 
#placeholder，占位符，在tensorflow中类似于函数参数，运行时必须传入值。
action = tf.placeholder("float", [None, output]) #操作，就是一维的了吧。。。None?
#Tensor("Placeholder_1:0", shape=(?, 3), dtype=float32) ？个结果

#定义CNN卷积神经网络 
def convolutional_neural_network(input_image):
    weights = {'w_conv1':tf.Variable(tf.zeros([8, 8, 4, 32])), #第一层矩阵, ???
            'w_conv2':tf.Variable(tf.zeros([4, 4, 32, 64])),
            'w_conv3':tf.Variable(tf.zeros([3, 3, 64, 64])),
            'w_fc4':tf.Variable(tf.zeros([3456, 784])),
            'w_out':tf.Variable(tf.zeros([784, output]))}

    biases = {'b_conv1':tf.Variable(tf.zeros([32])), #就最后一个是的吗？嗯。。。
            'b_conv2':tf.Variable(tf.zeros([64])), #他们弄好的，应该是最优的了吧
            'b_conv3':tf.Variable(tf.zeros([64])), 
            'b_fc4':tf.Variable(tf.zeros([784])), 
            'b_out':tf.Variable(tf.zeros([output]))}
    
    conv1 = tf.nn.relu(tf.nn.conv2d(input_image, weights['w_conv1'], strides = [1, 4, 4, 1], padding = "VALID") + biases['b_conv1'])
    conv2 = tf.nn.relu(tf.nn.conv2d(conv1, weights['w_conv2'], strides = [1, 2, 2, 1], padding = "VALID") + biases['b_conv2'])
    conv3 = tf.nn.relu(tf.nn.conv2d(conv2, weights['w_conv3'], strides = [1, 1, 1, 1], padding = "VALID") + biases['b_conv3'])
    conv3_flat = tf.reshape(conv3, [-1, 3456]) #原来3456是这样来的，直接reshape

    #上面是卷积，下面是一般矩陈乘法
    fc4 = tf.nn.relu(tf.matmul(conv3_flat, weights['w_fc4']) + biases['b_fc4'])
    output_layer = tf.matmul(fc4, weights['w_out']) + biases['b_out']
    return output_layer #输出层的结果就卷积加普通积出来了。但现在没运行。

#训练神经网络
def train_neural_network(input_image):
    predict_action = convolutional_neural_network(input_image) #把图片给卷积出一个特征结果来

    argmax = tf.placeholder("float", [None, output]) #占位
    gt = tf.placeholder("float", [None])

    #action = tf.reduce_sum(tf.mul(predict_action, argmax), reduction_indices = 1)
    action = tf.reduce_sum(tf.multiply(predict_action, argmax), reduction_indices = 1) #被换成了这个了。唉呀。。。还好有google...#这人经常换。看来还是明白思路重要。
    #这是用来取出tensor的，是的，取出action，但数据没灌入呢，包括argmax
    cost = tf.reduce_mean(tf.square(action - gt))
    optimizer = tf.train.AdamOptimizer(1e-6).minimize(cost)

    game = Game() #生成图片的，并且图片对应输入的
    D = deque() #

    _, image = game.step(MOVE_STAY) #reward, screen_image 
    #转换为灰度值
    image = cv2.cvtColor(cv2.resize(image, (100, 80)), cv2.COLOR_BGR2GRAY)
    #转换为2进制值
    ret, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
    #image = np.reshape(image, (80, 100, 1)) #底下有这个没有，复制过来 #嘿，还真不能reshape呢，这正是要的。。。
    input_image_data = np.stack((image, image, image, image), axis = 2) #???

    with tf.Session() as sess: #这里才开始真正的有数据
        sess.run(tf.initialize_all_variables()) #卷积的开始初始化了，必须的一步，并且输入了第一个操作

        saver = tf.train.Saver() #用来保存的

        n = 0
        hundred_rewards = 0
        number_hundred = 0
        epsilon = INITIAL_EPSILON #1.0

        while True:
            action_t = predict_action.eval(feed_dict={input_image : [input_image_data]})[0] #只要第0个，但前面为什么弄四个图片。。。
            #这是调用卷积普通积的，得出个特征/操作

            argmax_t = np.zeros([output], dtype=np.int) #3个int的
            
            if(random.random() <= epsilon): #随机的操作一次，刚开始必然
            #if(random.random() <= INITIAL_EPSILON): 
            #<=1.0, 必然如此，后面没有INITIAL_EPSILON变化，但有epsilon变化
            #原来之前是这里错了，一直都是随机嘛。。。真是。。。
                maxIndex = random.randrange(output) 
                #randrange(start, stop=None, step=1, _int=<class 'int'>)
                #结果是0, 1, 2这三个数。就是3以内的随机整数，偶尔这样即可
            else:
                maxIndex = np.argmax(action_t) 
                #根据卷积乘积出来的特征/预测action_t
                #然后根据某个轴，输出最大数的序数，从0开始，action_[0/1/2]三个哪个最大输出哪个的序号

            argmax_t[maxIndex] = 1 #最大的值的序号，在三个0中，最大的序号那个的值换为1，就形成了一个输入了

            if epsilon > FINAL_EPSILON: #>0.05
                epsilon -= (INITIAL_EPSILON - FINAL_EPSILON) / EXPLORE
                #-=(1-0.05)/500000，直到本来等于1的epsilon<=0.05为止

            #macOS需要事件循环，pygame的，否则白屏?这些问题啊。。。
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            reward, image = game.step(list(argmax_t)) #step(self, action) #
            #循环外的一次Image已经用完了，现在投入刚刚生成的指令需再生成一次

            image = cv2.cvtColor(cv2.resize(image, (100, 80)), cv2.COLOR_BGR2GRAY)
            #熟悉的转换再转换
            ret, image = cv2.threshold(image, 1, 255, cv2.THRESH_BINARY)
            image = np.reshape(image, (80, 100, 1))
            input_image_data1 = np.append(image, input_image_data[:, :, 0:3], axis = 2) #这个附加搞不懂了。为了udw凑够四维吗？

            D.append((input_image_data, argmax_t, reward, input_image_data1))

            if len(D) > REPLAY_MEMORY: #50万的上个输入图/输出的特征和奖励/下一个输入图
                D.popleft() #太多了就删除记忆

            if n > OBSERVE: #如果大于了设定的观测次数,50000，有了足够多的样品了
                minibatch = random.sample(D, BATCH) #从D中选100个作为sample
                #sample(population, k),从population中随机选择k个形成新列表

                input_image_data_batch = [d[0] for d in minibatch] #上次输入神经网络的图组
                argmax_batch = [d[1] for d in minibatch] #上次神经网络输出的特征/预测组，即这次输入游戏的组
                reward_batch = [d[2] for d in minibatch] #这次输入游戏后得的奖励组
                input_image_data1_batch = [d[3] for d in minibatch] #这次输入游戏后得的图组，即，这次输入神经网络的图组

                gt_batch = []

                out_batch = predict_action.eval(feed_dict = {input_image: input_image_data1_batch}) 
                #再用这次输入神经网络的图组来得到下次的游戏输入

                for i in range(0, len(minibatch)):
                #遍历得到的样品组（这时才是开始学习吧。。。慢的。。。）
                    gt_batch.append(reward_batch[i] + LEARNING_RATE * np.max(out_batch[i])) 
                    #这次输入游戏后的奖励+学习效率*预测的下次游戏输入

                optimizer.run(feed_dict = {gt : gt_batch, argmax : argmax_batch, input_image : input_image_data_batch})
                #这次的奖励（结果）与下次的预测，这次输入游戏的值，上次输入神经网络的图组
                #来进行优化，有上次输入神经网络的结果即这次的输入和这次的结果与下次的预测，还有上次输入神经网络的图组

            input_image_data = input_image_data1 
            #这次的输入神经网络的图组要输入了，之前用许多之前的“这次”来预测并优化过神经网络了，谁知道怎么优化的。。。
            n += 1

            if (n-50000) % 10000 == 0:
                saver.save(sess, 'game.cpk', global_step = n) #万次保存模型 
            if reward != 0:
                #print(n, "epsilon:", epsilon, ' ', 'action:', maxIndex, ' ', 'reward:', reward)
                hundred_rewards += reward
                number_hundred += 1
                if number_hundred % 100 == 0:
                    print(n, "epsilon:", epsilon, ' ', 'action:', maxIndex, ' ', '100rewards:', hundred_rewards)
                    hundred_rewards = 0
                #maxIndex, 012, 最大值的index，就是第几位是最大的，就是1, 
                #第0位最大不动，第1位最大左，第2位最大右
                #100不动，010 left, 001 right

train_neural_network(input_image) #第一个输入是随机了。。。后面的处理呢？

