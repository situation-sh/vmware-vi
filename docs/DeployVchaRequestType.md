# DeployVchaRequestType

The parameters of *FailoverClusterConfigurator.deployVcha_Task*. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_spec** | [**VchaClusterDeploymentSpec**](VchaClusterDeploymentSpec.md) |  | 

## Example

```python
from vmware_vi.models.deploy_vcha_request_type import DeployVchaRequestType

# TODO update the JSON string below
json = "{}"
# create an instance of DeployVchaRequestType from a JSON string
deploy_vcha_request_type_instance = DeployVchaRequestType.from_json(json)
# print the JSON string representation of the object
print DeployVchaRequestType.to_json()

# convert the object into a dict
deploy_vcha_request_type_dict = deploy_vcha_request_type_instance.to_dict()
# create an instance of DeployVchaRequestType from a dict
deploy_vcha_request_type_form_dict = deploy_vcha_request_type.from_dict(deploy_vcha_request_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


