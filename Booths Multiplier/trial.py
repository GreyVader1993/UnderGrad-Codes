from bitstring import BitArray


def isBitLengthCorrect(number, bitlength ):
	try:
		BitArray(int=number, length= bitlength)
		return False
	except:
		return True


def boothsMultiplicationAlgorithm(multiplier, multiplicand):
	#write your booths logic in this function

	bitlength_multiplier = 0
	bitlength_multiplicand = 0
	bitlength_negmultiplicand = 0

	while isBitLengthCorrect(multiplier, bitlength_multiplier):
		bitlength_multiplier += 1

	while isBitLengthCorrect(multiplicand, bitlength_multiplicand):
		bitlength_multiplicand += 1

	while isBitLengthCorrect(-multiplicand, bitlength_negmultiplicand):
		bitlength_negmultiplicand += 1

	bitlength = max(bitlength_multiplier, bitlength_multiplicand, bitlength_negmultiplicand)

	A = BitArray(int=0, length=bitlength)
	Q = BitArray(int=multiplier, length=bitlength)
	M = BitArray(int=multiplicand, length=bitlength)
	negM = BitArray(int= -multiplicand, length=bitlength)
	Qminus1 = BitArray(int=0, length=1)

	print A.bin, Q.bin, Qminus1.bin, M.bin, negM.bin
	print "\n\n\n"

	print "Booths Algorithm:\n"
	print A.bin,Q.bin,Qminus1.bin, M.bin, negM.bin

	for i in range(bitlength):
		print "cycle ",i
		checker = Q[-1:]+Qminus1

		if checker.bin == "10":
			print "Do A=A-M"
			print "---------------------------------------"
			A = BitArray(int= A.int + negM.int, length=bitlength)
			print A.bin,Q.bin,Qminus1.bin, M.bin, negM.bin
			print "---------------------------------------"
			print "Then shift"

		elif checker.bin == "01":
			print "Do A=A+M"
			print "---------------------------------------"			
			A = BitArray(int= A.int + M.int, length=bitlength)
			print A.bin,Q.bin,Qminus1.bin, M.bin, negM.bin
			print "---------------------------------------"
			print "Then shift"

		print "Now shifting ....."
		print "---------------------------------------"			

		#------------Arithmetic shift right --------
		P = A + Q + Qminus1
		msdP = P[0]
		P = P>>1
		P[0] = msdP


		A = P[:bitlength] #first bitlength bits of P
		Q = P[bitlength:-1] #second bitlength bits of P
		Qminus1 = P[-1:] #last bit of P
		#-------------------------------------------
		print A.bin,Q.bin,Qminus1.bin, M.bin, negM.bin
		print "---------------------------------------"			



	P = A + Q
	print "Result :",P.int
	return P.int

boothsMultiplicationAlgorithm(-5,-5)