# HostConfigFailed

Fault to indicate configuration of the host failed.  Configuration could have failed because of multiple reasons and individual failures will be reported in \\#failure.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failure** | [**List[MethodFault]**](MethodFault.md) |  | 

## Example

```python
from vmware_vi.models.host_config_failed import HostConfigFailed

# TODO update the JSON string below
json = "{}"
# create an instance of HostConfigFailed from a JSON string
host_config_failed_instance = HostConfigFailed.from_json(json)
# print the JSON string representation of the object
print HostConfigFailed.to_json()

# convert the object into a dict
host_config_failed_dict = host_config_failed_instance.to_dict()
# create an instance of HostConfigFailed from a dict
host_config_failed_form_dict = host_config_failed.from_dict(host_config_failed_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


