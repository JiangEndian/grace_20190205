#!/bin/bash


now_time_HM()
{
    date +%H%M
}


BEGINRING='/home/ed/beginring.mp3'
ENDRING='/home/ed/endring.mp3'

T1=$(($1*60))
T2=$(($2*60))

#echo sleep${T1}_and_sleep${T2}_all_${3}times
echo sleep${1}m_and_sleep${2}m_all_${3}times

run_begin_end_times() #一次是1小时，45MIN+15MIN
{
    for ((i=1;i<=$1;i++)) ;do
        echo $(now_time_HM)开始
        #play_once.bash $BEGINRING
        screenon.bash
        notify-send $(now_time_HM)开始
        #sleep 45m
        sleep $T1

        echo $(now_time_HM)休息
        notify-send '10S后开始休息。'
        sleep 10
        #play_once.bash $ENDRING
        screenoff.bash
        sleep 5
        screenoff.bash
        sleep $T2
    done
}

run_begin_end_times $3

exit 0

BEGINTIME='0600'
MORNING='0800'
AFTERNOON='1400'
EVENING='1900'

waiting4BEGINTIME()
{
    echo 等待时间:$1
    while :;do
        if [ $(now_time_HM) -eq $1 ];then
            #echo $(now_time_HM)
            break
        fi
        sleep 1
    done
}


newday()
{
    waiting4BEGINTIME $BEGINTIME #早上6点开始
    run_begin_end_times 1 #一节课（45MIN+15MIN），到6:45又多15分钟sleep，总到7:00
}

morning()
{
    waiting4BEGINTIME $MORNING
    run_begin_end_times 4 #四节课，到11:15又多15分钟sleep，总到12:00
}

afternoon()
{
    waiting4BEGINTIME $AFTERNOON
    run_begin_end_times 4 #四节课，到17:45(sleep至18:00)
}

evening()
{
    waiting4BEGINTIME $EVENING
    run_begin_end_times 2 #两节课，到20:45(sleep至21:00)
}


always_allday()
{
    while :;do
        if [ $(now_time_HM) -gt $AFTERNOON ]; then
            if [ $(now_time_HM) -lt $EVENING ]; then
                evening
                newday
                #morning
                #sleep 8h #到第二天才重新判断，因为，这种判断，只能从新一天开始(从小到大)
            else
                newday
                #morning
                #echo '已过晚上7点，将从明天开始哦～'
                #sleep 8h
            fi
        elif [ $(now_time_HM) -gt $MORNING ]; then
            afternoon
        elif [ $(now_time_HM) -gt $BEGINTIME ]; then
            morning
        else
            newday
        fi
    done
}

#always_allday

exit 0
