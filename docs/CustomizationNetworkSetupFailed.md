# CustomizationNetworkSetupFailed

Network setup failed in the guest during customization.  ***Since:*** VI API 2.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from vmware_vi.models.customization_network_setup_failed import CustomizationNetworkSetupFailed

# TODO update the JSON string below
json = "{}"
# create an instance of CustomizationNetworkSetupFailed from a JSON string
customization_network_setup_failed_instance = CustomizationNetworkSetupFailed.from_json(json)
# print the JSON string representation of the object
print CustomizationNetworkSetupFailed.to_json()

# convert the object into a dict
customization_network_setup_failed_dict = customization_network_setup_failed_instance.to_dict()
# create an instance of CustomizationNetworkSetupFailed from a dict
customization_network_setup_failed_form_dict = customization_network_setup_failed.from_dict(customization_network_setup_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


