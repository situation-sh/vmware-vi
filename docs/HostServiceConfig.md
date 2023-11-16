# HostServiceConfig

DataObject representing configuration for a particular service.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** | Key of the service to configure.  ***Since:*** vSphere API 4.0  | 
**startup_policy** | **str** | Startup policy which defines how the service be configured.  See @link Service.Policy for possible values.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.host_service_config import HostServiceConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HostServiceConfig from a JSON string
host_service_config_instance = HostServiceConfig.from_json(json)
# print the JSON string representation of the object
print HostServiceConfig.to_json()

# convert the object into a dict
host_service_config_dict = host_service_config_instance.to_dict()
# create an instance of HostServiceConfig from a dict
host_service_config_form_dict = host_service_config.from_dict(host_service_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


