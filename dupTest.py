from usefulFunctions import *

BC_list = getCuts('genomePieces/10m_digest_BC')
DE_list = getCuts('genomePieces/10m_digest_DE')
DFAD_list = getCuts('genomePieces/10m_digest_DFAD')
EDA_list = getCuts('genomePieces/10m_digest_EDA')

BC_set = set(BC_list)
DE_set = set(DE_list)
DFAD_set = set(DFAD_list)
EDA_set = set(EDA_list)

if (len(BC_list) != len(BC_set)):
	print "Duplicates in m BC"

if (len(DE_list) != len(DE_set)):
	print "Duplicates in m DE"

if (len(DFAD_list) != len(DFAD_set)):
	print "Duplicates in m DFAD"

if (len(EDA_list) != len(EDA_set)):
	print "Dupicates in m EDA"

