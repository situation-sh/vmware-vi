# NodeDeploymentSpec

The NodeDeploymentSpec class defines location specification of the nodes the VCHA Cluster along with Management vCenter Server information that manages node VM.  ***Since:*** vSphere API 6.5 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esx_host** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**datastore** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**public_network_port_group** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**cluster_network_port_group** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**folder** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | 
**resource_pool** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 
**management_vc** | [**ServiceLocator**](ServiceLocator.md) |  | [optional] 
**node_name** | **str** | nodeName here refers to a name that will be assigned to the VM to which this node will be deployed to.  ***Since:*** vSphere API 6.5  | 
**ip_settings** | [**CustomizationIPSettings**](CustomizationIPSettings.md) |  | 

## Example

```python
from vmware_vi.models.node_deployment_spec import NodeDeploymentSpec

# TODO update the JSON string below
json = "{}"
# create an instance of NodeDeploymentSpec from a JSON string
node_deployment_spec_instance = NodeDeploymentSpec.from_json(json)
# print the JSON string representation of the object
print NodeDeploymentSpec.to_json()

# convert the object into a dict
node_deployment_spec_dict = node_deployment_spec_instance.to_dict()
# create an instance of NodeDeploymentSpec from a dict
node_deployment_spec_form_dict = node_deployment_spec.from_dict(node_deployment_spec_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


