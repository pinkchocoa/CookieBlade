from youtube import *

reply = scrapData()
for i in range(0,len(reply)):
    reply[i] = vidInfo(reply[i])
    freply = reply[i].getDict()
    print('freply: ' , freply)

    print('======================================================================================================')
    print('======================================================================================================')

    rereply = channel.getChannelDetail(freply)
    for i in range(0,len(rereply)):
        rereply[i] = channel.getChannelStat(rereply[i])
        rereply[i] = channel.getChannelVid(rereply[i])
        print(rereply[i].channelDetail())
