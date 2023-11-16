# HostActiveDirectoryInfoDomainMembershipStatusEnum

Possible values: - `unknown`: The Active Directory integration provider does not support   domain trust checks. - `ok`: No problems with the domain membership. - `noServers`: The host thinks it's part of a domain,   but no domain controllers could be reached to confirm. - `clientTrustBroken`: The client side of the trust relationship is broken. - `serverTrustBroken`: The server side of the trust relationship is broken   (or bad machine password). - `inconsistentTrust`: Unexpected domain controller responded. - `otherProblem`: There's some problem with the domain membership.    ***Since:*** vSphere API 4.1 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


