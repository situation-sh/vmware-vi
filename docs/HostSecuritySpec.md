# HostSecuritySpec

DataObject used for configuring the Security settings  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_password** | **str** | Administrator password to configure  ***Since:*** vSphere API 4.0  | [optional] 
**remove_permission** | [**List[Permission]**](Permission.md) | Permissions to remove  ***Since:*** vSphere API 4.1  | [optional] 
**add_permission** | [**List[Permission]**](Permission.md) | Permissions to add  ***Since:*** vSphere API 4.1  | [optional] 

## Example

```python
from vmware_vi.models.host_security_spec import HostSecuritySpec

# TODO update the JSON string below
json = "{}"
# create an instance of HostSecuritySpec from a JSON string
host_security_spec_instance = HostSecuritySpec.from_json(json)
# print the JSON string representation of the object
print HostSecuritySpec.to_json()

# convert the object into a dict
host_security_spec_dict = host_security_spec_instance.to_dict()
# create an instance of HostSecuritySpec from a dict
host_security_spec_form_dict = host_security_spec.from_dict(host_security_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


