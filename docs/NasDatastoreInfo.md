# NasDatastoreInfo

Information details about a network-attached storage (NAS) datastore. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nas** | [**HostNasVolume**](HostNasVolume.md) |  | [optional] 

## Example

```python
from vmware_vi.models.nas_datastore_info import NasDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of NasDatastoreInfo from a JSON string
nas_datastore_info_instance = NasDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print NasDatastoreInfo.to_json()

# convert the object into a dict
nas_datastore_info_dict = nas_datastore_info_instance.to_dict()
# create an instance of NasDatastoreInfo from a dict
nas_datastore_info_form_dict = nas_datastore_info.from_dict(nas_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


