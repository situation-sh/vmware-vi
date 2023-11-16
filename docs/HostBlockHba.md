# HostBlockHba

This data object type describes the host bus adapter that provides block devices. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.host_block_hba import HostBlockHba

# TODO update the JSON string below
json = "{}"
# create an instance of HostBlockHba from a JSON string
host_block_hba_instance = HostBlockHba.from_json(json)
# print the JSON string representation of the object
print HostBlockHba.to_json()

# convert the object into a dict
host_block_hba_dict = host_block_hba_instance.to_dict()
# create an instance of HostBlockHba from a dict
host_block_hba_form_dict = host_block_hba.from_dict(host_block_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


