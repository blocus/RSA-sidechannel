#include <stdio.h>
#include "gmp.h"

int main(int argc, char const *argv[])
{
	mpz_t n, e, d, p, q, y, tmp;
	mpz_inits(y, tmp, NULL);
	mpz_init_set_str(n, "0x00c08e3f1534ba2d770021a38b8639c705c69d00c677bcd5f7e4b0023e5892c983", 0);
	mpz_init_set_str(e, "0x10001", 0);
	mpz_init_set_str(d, "0x009bf55a80b98125fbe17e5d714f9912696251ecb2fc4af3858467bdbe8736b6a9", 0);
	mpz_init_set_str(p, "0x00e5e2cc587a1d55c0c663276d2f3ab06f", 0);
	mpz_init_set_str(q, "0x00d66ddd446d7e521c9a550b0db6519a2d", 0);
	mpz_sub_ui(tmp, p, 1);
	mpz_mul_ui(y, tmp, 1);
	mpz_sub_ui(tmp, q, 1);
	mpz_mul(y, y, tmp);
	mpz_mul(tmp, e, d);
	mpz_mod(tmp, tmp, y);

	gmp_printf("tmp = %Zu\n", tmp);
	
	mpz_clears(n, e, d, p, q, y, tmp);
	return 0;
}