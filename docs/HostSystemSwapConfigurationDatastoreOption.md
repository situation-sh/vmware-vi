# HostSystemSwapConfigurationDatastoreOption

Use option to indicate that a user specified datastore may be used for system swap.  ***Since:*** vSphere API 5.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datastore** | **str** | The datastore to be used with this swap option.  This value should be always set when the encapsulating option is used, otherwise a call to *HostSystem.UpdateSystemSwapConfiguration* will result in a *InvalidArgument* fault.  ***Since:*** vSphere API 5.1  | 

## Example

```python
from vmware_vi.models.host_system_swap_configuration_datastore_option import HostSystemSwapConfigurationDatastoreOption

# TODO update the JSON string below
json = "{}"
# create an instance of HostSystemSwapConfigurationDatastoreOption from a JSON string
host_system_swap_configuration_datastore_option_instance = HostSystemSwapConfigurationDatastoreOption.from_json(json)
# print the JSON string representation of the object
print HostSystemSwapConfigurationDatastoreOption.to_json()

# convert the object into a dict
host_system_swap_configuration_datastore_option_dict = host_system_swap_configuration_datastore_option_instance.to_dict()
# create an instance of HostSystemSwapConfigurationDatastoreOption from a dict
host_system_swap_configuration_datastore_option_form_dict = host_system_swap_configuration_datastore_option.from_dict(host_system_swap_configuration_datastore_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


