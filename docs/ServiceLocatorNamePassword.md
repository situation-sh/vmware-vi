# ServiceLocatorNamePassword

The data object type specifies the username and password credential for authenticating to a service endpoint.  ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** | The username for Username-Password authentication  ***Since:*** vSphere API 6.0  | 
**password** | **str** | The password for Username-Password authentication  ***Since:*** vSphere API 6.0  | 

## Example

```python
from vmware_vi.models.service_locator_name_password import ServiceLocatorNamePassword

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceLocatorNamePassword from a JSON string
service_locator_name_password_instance = ServiceLocatorNamePassword.from_json(json)
# print the JSON string representation of the object
print ServiceLocatorNamePassword.to_json()

# convert the object into a dict
service_locator_name_password_dict = service_locator_name_password_instance.to_dict()
# create an instance of ServiceLocatorNamePassword from a dict
service_locator_name_password_form_dict = service_locator_name_password.from_dict(service_locator_name_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


