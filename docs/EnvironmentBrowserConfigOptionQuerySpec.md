# EnvironmentBrowserConfigOptionQuerySpec

Represent search criteria and filters on a *VirtualMachineConfigOption* object.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key found in the VirtualMachineConfigOptionDescriptor, obtained by invoking the *EnvironmentBrowser.QueryConfigOptionDescriptor* operation.  ***Since:*** vSphere API 6.0  | [optional] 
**host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**guest_id** | **List[str]** | The Guest OS IDs whose *VirtualMachineConfigOption* is requested *GuestOsIdentifier*  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.environment_browser_config_option_query_spec import EnvironmentBrowserConfigOptionQuerySpec

# TODO update the JSON string below
json = "{}"
# create an instance of EnvironmentBrowserConfigOptionQuerySpec from a JSON string
environment_browser_config_option_query_spec_instance = EnvironmentBrowserConfigOptionQuerySpec.from_json(json)
# print the JSON string representation of the object
print EnvironmentBrowserConfigOptionQuerySpec.to_json()

# convert the object into a dict
environment_browser_config_option_query_spec_dict = environment_browser_config_option_query_spec_instance.to_dict()
# create an instance of EnvironmentBrowserConfigOptionQuerySpec from a dict
environment_browser_config_option_query_spec_form_dict = environment_browser_config_option_query_spec.from_dict(environment_browser_config_option_query_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


