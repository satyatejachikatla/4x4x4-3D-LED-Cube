
set_bit_index_map = { 1 << bit_pos : bit_pos for bit_pos in range(32)}

def set_bit_index(x):

	return set_bit_index_map[x]

def index_to_pin_out(voxel_details,decoder_details):

	TOTAL_DECODERS        = decoder_details['TOTAL_DECODERS']
	DECODER_OUT_BITS_MASK = decoder_details['DECODER_OUT_BITS_MASK']
	DECODER_OUT_BITS      = decoder_details['DECODER_OUT_BITS']

	H , W , D  = voxel_details['grid_shape']
	h , w , d  = voxel_details['voxel_index']
	brightness = voxel_details['brightness']

	decoder_input  = 0
	select_decoder = 0

	if brightness <= 0 :
		return decoder_input , select_decoder

	acc = 1 << h * W +  w

	curr_decoder = 0

	while curr_decoder < TOTAL_DECODERS:
		masked_acc     = acc & DECODER_OUT_BITS_MASK
		acc            = acc >> DECODER_OUT_BITS
		select_decoder = select_decoder << 1
		curr_decoder += 1
		if masked_acc:
			select_decoder += 1
			decoder_input = set_bit_index(masked_acc)

			# End loop condition
			while curr_decoder < TOTAL_DECODERS:
				select_decoder = select_decoder << 1
				curr_decoder += 1


	return decoder_input , select_decoder