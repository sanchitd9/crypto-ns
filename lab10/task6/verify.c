#include <stdio.h>
#include <string.h>
#include <openssl/bn.h>

#define SHA_LENGTH 64
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
	BN_hex2bn(&n, "D753A40451F899A616484B6727AA9349D039ED0CB0B00087F1672886858C8E63DABCB14038E2D3F5ECA50518B83D3EC5991732EC188CFAF10CA6642185CB071034B052882B1F689BD2B18F12B0B3D2E7881F1FEF387754535F80793F2E1AAAA81E4B2B0DABB763B935B77D14BC594BDF514AD2A1E20CE29082876AAEEAD764D69855E8FDAF1A506C54BC11F2FD4AF29DBB7F0EF4D5BE8E16891255D8C07134EEF6DC2DECC48725868DD821E4B04D0C89DC392617DDF6D79485D80421709D6F6FFF5CBA19E145CB5657287E1C0D4157AAB7B827BBB1E4FA2AEF2123751AAD2D9B86358C9C77B573ADD8942DE4F30C9DEEC14E627E17C0719E2CDEF1F910281933");
	BN_hex2bn(&e, "10001");
	BN_hex2bn(&s, "3ebb214ca8b43c7fd92110c4da95626f3f62bb6aa2265ff797b05842c559f4f42388c071338ed12980a2a6648176346c3e206dca07ac393cf3d29684094b7cc7bc3f9ca9172d5ac0967c16f2c1a015379559bd0d2a41005c0b88619e2f8da7719617c91aa11ee21551b5aa4554fc76eb1146da6ddfdffb5435b85dfa8edd85859d1b4f1a761e035f1c27156e7cf5f8ee19f7c1bd3cb133ef94197e799f86412293666cdc18c1c4a1687d5032f75be24c2d9efe2f9e2a4835dee8f4a50822d3a256f9a5198d6f28460f5a67681e255e61f441618a783cd4a4249b6ee92cc84b666beef79d479f0a23ee423f676e7ff1f975e12af0880f0df214253315285a903a");
	BN_hex2bn(&m, "267021b6a8b383e8896700bad0970b31e8e46970b16bcab788d5e85e12623aed");

	// Print the original message
	printBN("Original Message:", m, 'h');

	// Decrypt the signature
	BN_mod_exp(dm, s, e, n, ctx);

	// Extract the last 64 characters (the remaining characters are part of the padding scheme)
	char *decrypt_str = BN_bn2hex(dm);
	char substr[100];
	strncpy(substr, decrypt_str + strlen(decrypt_str) - SHA_LENGTH, SHA_LENGTH);
	BN_hex2bn(&dm, substr);
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
