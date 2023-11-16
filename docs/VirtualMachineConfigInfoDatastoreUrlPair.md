# VirtualMachineConfigInfoDatastoreUrlPair

Contains the name of a datastore, and its local file path on the host currently affiliated with this virtual machine. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**url** | **str** |  | 

## Example

```python
from vmware_vi.models.virtual_machine_config_info_datastore_url_pair import VirtualMachineConfigInfoDatastoreUrlPair

# TODO update the JSON string below
json = "{}"
# create an instance of VirtualMachineConfigInfoDatastoreUrlPair from a JSON string
virtual_machine_config_info_datastore_url_pair_instance = VirtualMachineConfigInfoDatastoreUrlPair.from_json(json)
# print the JSON string representation of the object
print VirtualMachineConfigInfoDatastoreUrlPair.to_json()

# convert the object into a dict
virtual_machine_config_info_datastore_url_pair_dict = virtual_machine_config_info_datastore_url_pair_instance.to_dict()
# create an instance of VirtualMachineConfigInfoDatastoreUrlPair from a dict
virtual_machine_config_info_datastore_url_pair_form_dict = virtual_machine_config_info_datastore_url_pair.from_dict(virtual_machine_config_info_datastore_url_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


