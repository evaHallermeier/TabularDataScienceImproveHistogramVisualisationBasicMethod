def getDS_size(df):
  nb_cols = len(df.axes[1])
  nb_samples = len(df.axes[0])
  print(f"There are {nb_cols} columns")
  print(f"There are {nb_samples} samples")

def getFeatureInfo(df, f):
  print("Feature name: ", f)
  feature = df[f]
  rangeValues = feature.describe().max() - feature.describe().min()
  print(f"Amplitude of values: {rangeValues}")
  nb_samples=len(df.axes[0])
  counts = df[f].nunique()
  print("Nb of different values in the feature: ", counts)
  print(f"Range of values: {feature.min()}  - {df[f].max()}")
  print(f"Nb of samples for this feature : {feature.shape[0]}")