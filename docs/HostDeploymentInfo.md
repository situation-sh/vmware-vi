# HostDeploymentInfo

Data object describing the deployment information for a host.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**booted_from_stateless_cache** | **bool** | Flag indicating if the host was booted from stateless cache.  ***Since:*** vSphere API 6.5  | [optional] 

## Example

```python
from vmware_vi.models.host_deployment_info import HostDeploymentInfo

# TODO update the JSON string below
json = "{}"
# create an instance of HostDeploymentInfo from a JSON string
host_deployment_info_instance = HostDeploymentInfo.from_json(json)
# print the JSON string representation of the object
print HostDeploymentInfo.to_json()

# convert the object into a dict
host_deployment_info_dict = host_deployment_info_instance.to_dict()
# create an instance of HostDeploymentInfo from a dict
host_deployment_info_form_dict = host_deployment_info.from_dict(host_deployment_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


