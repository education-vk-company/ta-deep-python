lib3.so: 3.o
	gcc -fPIC -shared -o lib3.so 3.o
3.o: 3.c
	gcc -c -fPIC 3.c
clean:
	rm *.o lib3.so
