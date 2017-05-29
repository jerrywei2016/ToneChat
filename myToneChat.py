import json
from watson_developer_cloud import ConversationV1
from watson_developer_cloud import ToneAnalyzerV3

conversation = ConversationV1(
    username='dae6b8af-ba2c-4c15-bf5d-9dee1df50cec',
    password='TDVlJMMIF8nD',
    version='2017-04-21')
tone_analyzer = ToneAnalyzerV3(
    username='38b0d824-40f8-40a9-88e0-afa02bbf33cc',
    password='S3o4gt65pURp',
    version='2016-02-11')

workspace_id = '2cef533b-b4fa-4d3e-b008-1c38aa80a1cd'


convContext = ''

def chat(msg):
    global convContext
    #first time start the conversation
    if (convContext == ''):
        response = conversation.message(workspace_id=workspace_id,
            message_input={'text': ''})
        convContext = response['context']
        print('++++', response['output']['text'])

    response = conversation.message(workspace_id=workspace_id,
        message_input={'text': msg}, context=convContext)
    convContext = response['context']
    return response

def printFullResponse(response):
    print(json.dumps(response, indent=2))

def printChat(msg):
    response = chat(msg)
    # printFullResponse(response)
    print('++++', response['output']['text'])

def tone(msg):
    utterances = [{'text': msg}]
    response = tone_analyzer.tone_chat(utterances)
    return response

def toneChat(msg):
    chatResp = chat(msg)
    toneResp = tone(msg)
    printChat(msg)
    printFullResponse(toneResp)



toneChat('I am very happy')
toneChat('I am very sad')
toneChat('I am very angry')
