# OvfConsumerOstNode

A node in the OVF section tree.  This class represents a node on which OVF sections can be defined. The possible node types are OstNodeType.envelope, OstNodeType.virtualSystem or OstNodeType.virtualSystemCollection, corresponding to the identically named OVF element types.  Since the node contains a list of children, it can also be regarded as a tree. This tree mirrors the structure of the OVF descriptor. It is provided to OVF consumers as a more convenient way to navigate and modify the OVF than by working directly on the XML.  ***Since:*** vSphere API 5.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The OVF id of the Content (VirtualSystem or VirtualSystemCollection) element.  Empty on the envelope node.  ***Since:*** vSphere API 5.0  | 
**type** | **str** | The type of the node.  Possible values are defined in the OstNodeType enum.  Since the OstNode tree structure mirrors the structure of the OVF descriptor, only one Envelope node is defined, and it is always the root of the tree.  ***Since:*** vSphere API 5.0  | 
**section** | [**List[OvfConsumerOvfSection]**](OvfConsumerOvfSection.md) | The list of sections on this node.  ***Since:*** vSphere API 5.0  | [optional] 
**child** | [**List[OvfConsumerOstNode]**](OvfConsumerOstNode.md) | The list of child nodes.  As dictated by OVF, this list is subject to the following rules: - The Envelope node must have exactly one child. - VirtualSystemCollection nodes may have zero or more children. - VirtualSystem nodes must have no children.    ***Since:*** vSphere API 5.0  | [optional] 
**entity** | [**ManagedObjectReference**](ManagedObjectReference.md) |  | [optional] 

## Example

```python
from vmware_vi.models.ovf_consumer_ost_node import OvfConsumerOstNode

# TODO update the JSON string below
json = "{}"
# create an instance of OvfConsumerOstNode from a JSON string
ovf_consumer_ost_node_instance = OvfConsumerOstNode.from_json(json)
# print the JSON string representation of the object
print OvfConsumerOstNode.to_json()

# convert the object into a dict
ovf_consumer_ost_node_dict = ovf_consumer_ost_node_instance.to_dict()
# create an instance of OvfConsumerOstNode from a dict
ovf_consumer_ost_node_form_dict = ovf_consumer_ost_node.from_dict(ovf_consumer_ost_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


