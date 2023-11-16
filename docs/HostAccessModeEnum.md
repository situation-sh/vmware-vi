# HostAccessModeEnum

Defines different access modes that a user may have on the host for direct host connections.  The assumption here is that when the host is managed by vCenter, we don't need fine-grained control on local user permissions like the interface provided by *AuthorizationManager*.  Possible values: - `accessNone`: Indicates that the user has no explicitly defined permissions or roles.      This is used when we want to remove all permissions for some user.      Note that this is not the same as *accessNoAccess*. - `accessAdmin`: Describes a propagating Admin role on the root inventory object   (root folder) on the host, and no other non-Admin role on any other   object.      The same permissions are needed to login to local or remote   shell (ESXiShell or SSH). - `accessNoAccess`: Describes a propagating NoAccess role on the root inventory object   (root folder) on the host, and no other roles.      Even if the user has another (redundant) NoAccess role on some other   inventory object, then the access mode for this user will be   classified as *accessOther*.      This mode may be used to restrict a specific user account without   restricting the access mode for the group to which the user belongs. - `accessReadOnly`: Describes a propagating ReadOnly role on the root inventory object   (root folder) on the host, and no other roles.      Even if the user has another (redundant) ReadOnly role on some other   inventory object, then the access mode for this user will be   *accessOther*. - `accessOther`: Describes a combination of one or more roles/permissions which are   none of the above.    ***Since:*** vSphere API 6.0 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


