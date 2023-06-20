from time import time

def calculate_mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                    error += 1

    return error

def calculate_speed(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_taken = round(time_delay, 2)
    speed = len(user_input) / time_taken
    return round(speed)

def main():
    test = ["Girish is typing","If there's one thing a rough patch. We even curatenced the same things as you can go a long way."]
    test_sentence = test[0]

    print("***** Typing Speed *****")
    print(test_sentence)
    print()

    time_start = time()
    user_input = input()
    time_end = time()

    speed = calculate_speed(time_start, time_end, user_input)
    error = calculate_mistake(test_sentence, user_input)

    print("Speed: {} words/sec".format(speed))
    print("Error: {}".format(error))

if __name__ == '__main__':
    main()