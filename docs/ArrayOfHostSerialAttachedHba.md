# ArrayOfHostSerialAttachedHba

A boxed array of *HostSerialAttachedHba*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[HostSerialAttachedHba]**](HostSerialAttachedHba.md) |  | 

## Example

```python
from vmware_vi.models.array_of_host_serial_attached_hba import ArrayOfHostSerialAttachedHba

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfHostSerialAttachedHba from a JSON string
array_of_host_serial_attached_hba_instance = ArrayOfHostSerialAttachedHba.from_json(json)
# print the JSON string representation of the object
print ArrayOfHostSerialAttachedHba.to_json()

# convert the object into a dict
array_of_host_serial_attached_hba_dict = array_of_host_serial_attached_hba_instance.to_dict()
# create an instance of ArrayOfHostSerialAttachedHba from a dict
array_of_host_serial_attached_hba_form_dict = array_of_host_serial_attached_hba.from_dict(array_of_host_serial_attached_hba_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


