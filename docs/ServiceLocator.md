# ServiceLocator

This data object type specifies the information of a service endpoint as well as the parameters needed to locate and login to to the service endpoint.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_uuid** | **str** | Unique ID of the instance to which the service belongs.  For instances that support the vSphere API, this is the same as the value found in *AboutInfo.instanceUuid*.  ***Since:*** vSphere API 6.0  | 
**url** | **str** | URL used to access the service endpoint  ***Since:*** vSphere API 6.0  | 
**credential** | [**ServiceLocatorCredential**](ServiceLocatorCredential.md) |  | 
**ssl_thumbprint** | **str** | The sslThumbprint of the service endpoint  ***Since:*** vSphere API 6.0  | [optional] 

## Example

```python
from vmware_vi.models.service_locator import ServiceLocator

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocator from a JSON string
service_locator_instance = ServiceLocator.from_json(json)
# print the JSON string representation of the object
print ServiceLocator.to_json()

# convert the object into a dict
service_locator_dict = service_locator_instance.to_dict()
# create an instance of ServiceLocator from a dict
service_locator_form_dict = service_locator.from_dict(service_locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


