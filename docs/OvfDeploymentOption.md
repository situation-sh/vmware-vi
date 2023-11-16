# OvfDeploymentOption

A deployment option as defined in the OVF specfication.  This corresponds to the Configuration element of the DeploymentOptionSection in the specification.  ***Since:*** vSphere API 4.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the deployment option, corresponding to the ovf:id attribute in the OVF descriptor  ***Since:*** vSphere API 4.0  | 
**label** | **str** | A localized label for the deployment option  ***Since:*** vSphere API 4.0  | 
**description** | **str** | A localizable description for the deployment option.  ***Since:*** vSphere API 4.0  | 

## Example

```python
from vmware_vi.models.ovf_deployment_option import OvfDeploymentOption

# TODO update the JSON string below
json = "{}"
# create an instance of OvfDeploymentOption from a JSON string
ovf_deployment_option_instance = OvfDeploymentOption.from_json(json)
# print the JSON string representation of the object
print OvfDeploymentOption.to_json()

# convert the object into a dict
ovf_deployment_option_dict = ovf_deployment_option_instance.to_dict()
# create an instance of OvfDeploymentOption from a dict
ovf_deployment_option_form_dict = ovf_deployment_option.from_dict(ovf_deployment_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


