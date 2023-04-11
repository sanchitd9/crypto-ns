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
	BIGNUM *p, *q, *n, *e, *d, *phi, *res;
	BIGNUM *p_minus_one, *q_minus_one;

	// Allocate memory
	p           = BN_new();
	q           = BN_new();
	n           = BN_new();
	e           = BN_new();
	d           = BN_new();
	phi         = BN_new();
	res         = BN_new();
	p_minus_one = BN_new();
	q_minus_one = BN_new();

	// Initialize the variables
	BN_hex2bn(&p, "F7E75FDC469067FFDC4E847C51F452DF");
	BN_hex2bn(&q, "E85CED54AF57E53E092113E62F436F4F");
	BN_hex2bn(&e, "0D88C3");
	
	// Calculate (p-1) and (q-1)
	BN_sub(p_minus_one, p, BN_value_one());
	BN_sub(q_minus_one, q, BN_value_one());
	
	// Calculate n and phi(n)
	BN_mul(n, p, q, ctx);
	BN_mul(phi, p_minus_one, q_minus_one, ctx);

	// Check whether e and phi(n) are relatively prime.
	// If not, exit the program
	BN_gcd(res, phi, e, ctx);

	if (!BN_is_one(res)) {
		exit(0);
	}

	// Calculate the private key
	BN_mod_inverse(d, e, phi, ctx);
	printBN("Private key (hex):", d, 'h');
	printBN("Private key (decimal):", d, 'd');

	// Free memory
	BN_clear_free(p);
	BN_clear_free(q);
	BN_clear_free(n);
	BN_clear_free(e);
	BN_clear_free(d);
	BN_clear_free(phi);
	BN_clear_free(res);
	BN_clear_free(p_minus_one);
	BN_clear_free(q_minus_one);


	return 0;
}
