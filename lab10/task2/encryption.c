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
	BIGNUM *n, *e, *d, *c, *m, *dm;

	// Allocate memory
	n  = BN_new();
	e  = BN_new();
	d  = BN_new();
	m  = BN_new();
	c  = BN_new();
	dm = BN_new();

	// Initialize the variables
	BN_hex2bn(&n, "DCBFFE3E51F62E09CE7032E2677A78946A849DC4CDDE3A4D0CB81629242FB1A5");
	BN_hex2bn(&e, "010001");
	BN_hex2bn(&d, "74D806F9F3A62BAE331FFE3F0A68AFE35B3D2E4794148AACBC26AA381CD7D30D");
	BN_hex2bn(&m, "4120746f702073656372657421");

	// Print the message
	printBN("Original Message:", m, 'h');
	printf("\n----------------------------------------------------\n");

	// Encrypt the message
	BN_mod_exp(c, m, e, n, ctx);
	printBN("Encryption result (hex):", c, 'h');
	printBN("Encryption result (decimal):", c, 'd');
	printf("\n----------------------------------------------------\n");

	// Decrypt the message
	BN_mod_exp(dm, c, d, n, ctx);
	printBN("Decryption result (for verification):", dm, 'h');

	// Free memory
	BN_clear_free(n);
	BN_clear_free(e);
	BN_clear_free(d);
	BN_clear_free(m);
	BN_clear_free(c);
	BN_clear_free(dm);

	return 0;
}
