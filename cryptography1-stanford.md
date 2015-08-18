#Cryptography 1
## Introduction

### Course Objectives
1. Learn how _crypto primitives_ work
2. Learn how to use them to _reason_ correctly about security

### Course Overview
Information on the WWW is transmitted using __HTTP__ and encrypted with __SSL/TSL__. This _encryption_ ensures:
* no eavesdropping
* no tampering

## Secure Socket Layer / TLS
Has two parts:
* 1. Handshake protocol - __establish a shared secret key using public-key cryptography__ (2nd part of course)
* 2. Record layer - __transmit data using shared secret key__ - ensure _confidentiality_ and _integrity_ (1st part of course)
* data communication and file storage are _philosophically_ the same. Alice today is sending a message to Alice in the future... via an encrypted file she wants to access later.

### Building Block - Symmmetric Encryption
* Alice and Bob share a secret key __k__ which only they know and an attacker does not.

#### Encryption algorthim is publically available! Only the secret key is secret! 
* E, D - encryption algorithm, decryption algorithm : cipher - k 128 bit key
* m, c - message in plain text, ciphertext
* E(k,m) = c, D(k,c) = m
* c gets sent over the network from Alice to Bob
* Use cases:
  * __single use keys__ (encrypted email)
  * __multi use keys__ (encrypted files, based on machine)

__END OF OVERVIEW__

#What is Cryptography?
__Theorem:__ _Anything that can be done with a trusted authority can be done without one._

###Zero Knowledge (Proof of Knowledge)
Alice has a large number N which is the product of two large prime numbers p and q:
```
N = p x q
```
Imagine __p__ and __q__ are thousands of digits long. It is easy to calculate __N__ by multiplying __p x q__ but factoring __N__ to get _p_ and _q_ is quite difficult. In cryptography, Alice knows N, p, and q, but Bob only knows N. Alice can prove to Bob she knows p and q but Bob never knows what they are.
