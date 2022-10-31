import h5py

f = h5py.File('/usr/data/Co60_120s.h5', 'r')

print("H5 Keys")
print(list(f.keys()))
print()

for key in list(f.keys()):
    dset = f[key]

    print(f"dset name: {dset.name}")
    print(f"dset shape: {dset.shape}")
    print(f"dset dtype: {dset.dtype}")
    print()


#print(f"Raw data: {index}")
print(f['raw_data'][0,:])
print(len(f['raw_data'][0,:]))