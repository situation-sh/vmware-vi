# ArrayOfHostBlockHba

A boxed array of *HostBlockHba*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostBlockHba]**](HostBlockHba.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_block_hba import ArrayOfHostBlockHba

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostBlockHba from a JSON string
array_of_host_block_hba_instance = ArrayOfHostBlockHba.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostBlockHba.to_json()

# convert the object into a dict
array_of_host_block_hba_dict = array_of_host_block_hba_instance.to_dict()
# create an instance of ArrayOfHostBlockHba from a dict
array_of_host_block_hba_form_dict = array_of_host_block_hba.from_dict(array_of_host_block_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


