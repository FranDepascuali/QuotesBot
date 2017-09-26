#!/usr/bin/env python
# -*- coding: utf-8 -*-
from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
import sys
reload(sys)
sys.setdefaultencoding('utf8')
sys.path.append("/Users/FranDepascuali/Documents/Projects/Coding/wikiquotes-python-api")
import directory
import wikiquotes
import english
import spanish
from yowsup.layers.protocol_messages.protocolentities  import TextMessageProtocolEntity
import unidecode

class EchoLayer(YowInterfaceLayer):

    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):

        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        request_text = messageProtocolEntity.getBody()
        try:
            (author, raw_language) = request_text.rsplit(" ", 1)
            author = author.strip()
            raw_language = unicode(raw_language.strip())
            answer = wikiquotes.random_quote(author, raw_language)
        except Exception as e:
            print e
            answer = "Ups! No entendí eso. Escribime Autor Idioma! Ejemplo: Borges español"
            pass

        outgoingMessageProtocolEntity = TextMessageProtocolEntity(
            answer,
            to = messageProtocolEntity.getFrom()
        )

        self.toLower(outgoingMessageProtocolEntity)

        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))

    @ProtocolEntityCallback("receipt")
    def onReceipt(self, entity):
        self.toLower(entity.ack())

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
