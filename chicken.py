import discord

import random

import math




client = discord.Client()







@client.event

async def on_ready():

    print(client.user.id)

    print("ready")

    game = discord.Game("뜨거운 기름속에서 열일")

    await client.change_presence(status=discord.Status.online, activity=game)










@client.event

async def on_message(message):

    if message.content.startswith("!팀나누기"):

        mode = message.content.split(" ")[1]

        people = message.content.split(" ")[2]

        person = len(people.split(","))




        numbers = list(range(0,person))

        rand = []




        while len(rand) < person:

            num = random.choice(numbers)

            if not num in rand:

                rand.append(num)




        result = ""

        text = []




        if mode == "스쿼드":

            x = 0

            for i in rand :

                teamlocation = math.floor(i / 4) + 1

                text.append(str(teamlocation) + people.split(",")[x])

                x += 1

            j = 0

            while j < math.floor(person / 4) + 1:

                x = 0

                for i in text:

                    if int(i[0:1]) == j + 1:

                        result = result + str(i[0:1]) + "팀 " + people.split(",")[x] + "\n"

                    x += 1

                j += 1

        elif mode == "삼쿼드":

            x = 0

            for i in rand :

                teamlocation = math.floor(i / 3) + 1

                text.append(str(teamlocation) + people.split(",")[x])

                x += 1

            j = 0

            while j < math.floor(person / 3) + 1:

                x = 0

                for i in text:

                    if int(i[0:1]) == j + 1:

                        result = result + str(i[0:1]) + "팀 " + people.split(",")[x] + "\n"

                    x += 1

                j += 1

        elif mode == "듀오":

            x = 0

            for i in rand :

                teamlocation = math.floor(i / 2) + 1

                text.append(str(teamlocation) + people.split(",")[x])

                x += 1

            j = 0

            while j < math.floor(person / 2) + 1:

                x = 0

                for i in text:

                    if int(i[0:1]) == j + 1:

                        result = result + str(i[0:1]) + "팀 " + people.split(",")[x] + "\n"

                    x += 1

                j += 1

        else :

            await message.channel.send("올바른 명령어를 입력해 주세요.")

            

        await message.channel.send(result)




client.run("NjUwOTI5OTEyNTIxMTYyNzc0.XeTg7g.EvFXfXWL5QhOf2y5oN_ml7K4Ak4")
