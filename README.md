# Whatsapp Server

Plan for Phase 1

## Requirements

Need to build a chatting application

Features
1. Last Seen
2. Support to send media messages
3. Message encryption

DB (To save states, if client is unavailable)

A -> Message server (multiple, horizontally scalable) -< B (Need load balancer)

Duplex connection (Use websocket) - TCP/UDP/Websocket/Long Polling


Message server logic

Need to use kafka (pub/sub) cluster with topic for each user

Last Seen Logic

Need to store uid timestamp in a db

To store media, have a HTTP server. Use hash id for client B

## References

https://www.youtube.com/watch?v=L7LtmfFYjc4
