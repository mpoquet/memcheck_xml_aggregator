all: crash.xml leak.xml

crash.xml: errors
	valgrind --leak-check=full --xml=yes --xml-file=$@ ./$< crash

leak.xml: errors
	valgrind --leak-check=full --xml=yes --xml-file=$@ ./$<

errors: errors.cpp
	${CXX} -O0 -o $@ $<

