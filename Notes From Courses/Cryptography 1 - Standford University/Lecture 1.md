## Examples of Cryptography in daily life:
- Web traffic: HTTPS
- Wireless Traffic: 802.11i WPA2, GSM, Bluetooth
- Encrypting files on disk: EFS, TrueCrypt
- Content Protection (eg DVD, Blu-ray): Content Scrambling System*, AACS
- User Authentication
- Secure Communication: HTTPS/HTTP using SSL/TLS
  - Goals of HTTPS:
    - Make sure eavesdropping on the data is impossible.
    - Make modifying data in the network by an attacker impossible
  - TLS has 2 main parts:
    - Handshake Protocol: Establishing a shared secure key using public-key cryptography
    - Record Layer: Actually transmitting the data using the agreed upon key
  - Protecting data on storage:
    - Goals of stored file cryptography:
      - Make sure the clear data is unaccessible even if disk is stolen
      - Make sure that any modification on the encrypted file by the attacker is noticable to the owner
    - These goals ensure stored file cryptography ensure confidentiality and integrity of the files.


## Building block:
The building blocks of Symmetric Encryption are :-
1. Has a secret key K, that is known only to the communicating parties.
2. Has a cipher system which consists of a encryption algorithm and decryption algorithm
3. Encryption algorithm takes the clear text and the key as input and produces the cipher text
4. Decryption algorithm takes the cipher text and the key as input and produces the clear text
5. Cipher system are publicly known to everyone and the only thing keep secret is the key K.
	
Some typical use cases of symmetric encryption:
- One time key: A symmetric key is generated and used for encyption of each single message. Since the key is used for one time only, generation of such keys are fairly simple and efficient. Example of use case are emails.

- Many time key: A single symmetric key is generated and used for multiple encryptions. Since the key is used mutiple times, multiple steps are needed to ensure that the key genearted is safe and secured. Example of use case are file encryptions.
		


*Content Scrambling System (CSS) turns out to be fairly easy to be broken using methods of cryptanalysis
