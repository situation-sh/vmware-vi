# VmFailedUpdatingSecondaryConfig

This event records after a failover the new new primary failed to update the config of the secondary vm.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.vm_failed_updating_secondary_config import VmFailedUpdatingSecondaryConfig

# TODO update the JSON string below
json = "{}"
# create an instance of VmFailedUpdatingSecondaryConfig from a JSON string
vm_failed_updating_secondary_config_instance = VmFailedUpdatingSecondaryConfig.from_json(json)
# print the JSON string representation of the object
print VmFailedUpdatingSecondaryConfig.to_json()

# convert the object into a dict
vm_failed_updating_secondary_config_dict = vm_failed_updating_secondary_config_instance.to_dict()
# create an instance of VmFailedUpdatingSecondaryConfig from a dict
vm_failed_updating_secondary_config_form_dict = vm_failed_updating_secondary_config.from_dict(vm_failed_updating_secondary_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


