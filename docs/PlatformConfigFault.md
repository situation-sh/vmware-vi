# PlatformConfigFault

A PlatformConfigFault is a catch-all fault indicating that some error has occurred regarding the configuration of the host.  Data about the fault is available and will be presented as a platform specific string.  This information carried by this fault cannot be localized. Most likely this information will already have been localized to the locale of the server that generated this fault. Where possible, a more specific fault will be thrown. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**text** | **str** | Platform specific text string describing this error.  | 

## Example

```python
from vmware_vi.models.platform_config_fault import PlatformConfigFault

# TODO update the JSON string below
json = "{}"
# create an instance of PlatformConfigFault from a JSON string
platform_config_fault_instance = PlatformConfigFault.from_json(json)
# print the JSON string representation of the object
print PlatformConfigFault.to_json()

# convert the object into a dict
platform_config_fault_dict = platform_config_fault_instance.to_dict()
# create an instance of PlatformConfigFault from a dict
platform_config_fault_form_dict = platform_config_fault.from_dict(platform_config_fault_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


