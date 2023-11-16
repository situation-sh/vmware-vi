# RegisterHealthUpdateProviderRequestType

The parameters of *HealthUpdateManager.RegisterHealthUpdateProvider*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The provider name. Should follow Java package naming convention to minimize name clashes with currently registered providers. For example, \&quot;com.vmware.HealthUpdateProvider\&quot;.  | 
**health_update_info** | [**List[HealthUpdateInfo]**](HealthUpdateInfo.md) | The list of healthUpdateInfo that can be reported in healthUpdates.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.register_health_update_provider_request_type import RegisterHealthUpdateProviderRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterHealthUpdateProviderRequestType from a JSON string
register_health_update_provider_request_type_instance = RegisterHealthUpdateProviderRequestType.from_json(json)
# print the JSON string representation of the object
print RegisterHealthUpdateProviderRequestType.to_json()

# convert the object into a dict
register_health_update_provider_request_type_dict = register_health_update_provider_request_type_instance.to_dict()
# create an instance of RegisterHealthUpdateProviderRequestType from a dict
register_health_update_provider_request_type_form_dict = register_health_update_provider_request_type.from_dict(register_health_update_provider_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


