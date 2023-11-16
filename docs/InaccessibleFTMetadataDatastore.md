# InaccessibleFTMetadataDatastore

An InaccessibleFTMetadataDatastore exception is thrown if the datastore corresponding to the specified FT Metadata Datastore path isn't currently accessible.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.inaccessible_ft_metadata_datastore import InaccessibleFTMetadataDatastore

# TODO update the JSON string below
json = "{}"
# create an instance of InaccessibleFTMetadataDatastore from a JSON string
inaccessible_ft_metadata_datastore_instance = InaccessibleFTMetadataDatastore.from_json(json)
# print the JSON string representation of the object
print InaccessibleFTMetadataDatastore.to_json()

# convert the object into a dict
inaccessible_ft_metadata_datastore_dict = inaccessible_ft_metadata_datastore_instance.to_dict()
# create an instance of InaccessibleFTMetadataDatastore from a dict
inaccessible_ft_metadata_datastore_form_dict = inaccessible_ft_metadata_datastore.from_dict(inaccessible_ft_metadata_datastore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


