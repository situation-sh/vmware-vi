# ArrayOfVirtualMachineConfigInfoDatastoreUrlPair

A boxed array of *VirtualMachineConfigInfoDatastoreUrlPair*. To be used in *Any* placeholders. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[VirtualMachineConfigInfoDatastoreUrlPair]**](VirtualMachineConfigInfoDatastoreUrlPair.md) |  | 

## Example

```python
from vmware_vi.models.array_of_virtual_machine_config_info_datastore_url_pair import ArrayOfVirtualMachineConfigInfoDatastoreUrlPair

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayOfVirtualMachineConfigInfoDatastoreUrlPair from a JSON string
array_of_virtual_machine_config_info_datastore_url_pair_instance = ArrayOfVirtualMachineConfigInfoDatastoreUrlPair.from_json(json)
# print the JSON string representation of the object
print ArrayOfVirtualMachineConfigInfoDatastoreUrlPair.to_json()

# convert the object into a dict
array_of_virtual_machine_config_info_datastore_url_pair_dict = array_of_virtual_machine_config_info_datastore_url_pair_instance.to_dict()
# create an instance of ArrayOfVirtualMachineConfigInfoDatastoreUrlPair from a dict
array_of_virtual_machine_config_info_datastore_url_pair_form_dict = array_of_virtual_machine_config_info_datastore_url_pair.from_dict(array_of_virtual_machine_config_info_datastore_url_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


