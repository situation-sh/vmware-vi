# HostServiceSourcePackage


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source_package_name** | **str** | The name of the source package  ***Since:*** vSphere API 5.0  | 
**description** | **str** | The description of the source package  ***Since:*** vSphere API 5.0  | 

## Example

```python
from vmware_vi.models.host_service_source_package import HostServiceSourcePackage

# TODO update the JSON string below
json = "{}"
# create an instance of HostServiceSourcePackage from a JSON string
host_service_source_package_instance = HostServiceSourcePackage.from_json(json)
# print the JSON string representation of the object
print HostServiceSourcePackage.to_json()

# convert the object into a dict
host_service_source_package_dict = host_service_source_package_instance.to_dict()
# create an instance of HostServiceSourcePackage from a dict
host_service_source_package_form_dict = host_service_source_package.from_dict(host_service_source_package_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


