#include <stdio.h>
#include <openssl/bn.h>

#define NBITS 512

void printBN(char *msg, BIGNUM *a, char type) {
	char *number_str;
	if (type == 'd') {
		number_str = BN_bn2dec(a);
	}
	else if (type == 'h') {
		number_str = BN_bn2hex(a);
	}

	printf("%s %s\n", msg, number_str);
	OPENSSL_free(number_str);
}

int main() {
	BN_CTX *ctx = BN_CTX_new();
	
	// Declare the numbers
	BIGNUM *n, *e, *s, *m, *dm;

	// Allocate memory
	n  = BN_new();
	e  = BN_new();
	s  = BN_new();
	m  = BN_new();
	dm = BN_new();

	// Initialize the variables
	BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");
	BN_hex2bn(&e, "010001");
	BN_hex2bn(&s, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6803F");
	BN_hex2bn(&m, "4c61756e63682061206d697373696c652e");

	// Print the original message
	printBN("Original Message:", m, 'h');

	// Decrypt the signature
	BN_mod_exp(dm, s, e, n, ctx);
	printBN("Decryption:", dm, 'h');

	if (BN_cmp(m, dm) == 0) {
		printf("The signature is valid.\n");
	}
	else {
		printf("Invalid signature!\n");
	}

	// Free memory
	BN_clear_free(n);
	BN_clear_free(e);
	BN_clear_free(s);
	BN_clear_free(m);
	BN_clear_free(dm);

	return 0;
}
