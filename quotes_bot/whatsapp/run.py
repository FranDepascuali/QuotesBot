from yowsup.stacks                             import YowStackBuilder
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.stacks                             import YowStack
from yowsup.common                             import YowConstants
from yowsup.layers                             import YowLayerEvent
from yowsup                                    import env
from layer                                     import EchoLayer
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_presence           import YowPresenceProtocolLayer
from yowsup.env                                import YowsupEnv

#Deccomentare per log
#import logging
#logging.basicConfig(level=logging.DEBUG)

CREDENTIALS = ("4368181538553", "WdJbpG+GFqgP08rhXX7vGxnYBTU=") # replace with your phone and password

if __name__==  "__main__":
    stackBuilder = YowStackBuilder()

    stack = stackBuilder\
        .pushDefaultLayers(True)\
        .push(EchoLayer)\
        .build()

    stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)       #setting credentials
    stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))          #sending the connect signal
    stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])           #whatsapp server address
    stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
    stack.setProp(YowCoderLayer.PROP_RESOURCE, YowsupEnv.getCurrent().getResource())  #info about us as WhatsApp client

    stack.loop( timeout = 2.5, discrete = 2.5 )                                       #this is the program mainloop
