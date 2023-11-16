# PMemDatastoreInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pmem** | [**HostPMemVolume**](HostPMemVolume.md) |  | 

## Example

```python
from vmware_vi.models.p_mem_datastore_info import PMemDatastoreInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PMemDatastoreInfo from a JSON string
p_mem_datastore_info_instance = PMemDatastoreInfo.from_json(json)
# print the JSON string representation of the object
print PMemDatastoreInfo.to_json()

# convert the object into a dict
p_mem_datastore_info_dict = p_mem_datastore_info_instance.to_dict()
# create an instance of PMemDatastoreInfo from a dict
p_mem_datastore_info_form_dict = p_mem_datastore_info.from_dict(p_mem_datastore_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


