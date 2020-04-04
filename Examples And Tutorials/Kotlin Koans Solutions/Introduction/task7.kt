fun sendMessageToClient(client: Client?, message: String?, mailer: Mailer) {
    if (client == null || message == null) return
    
    // Since `client` and `message` have already been null checked, no need for safe-call.
    // We know they are not null
    val info: PersonalInfo = client.personalInfo ?: return
    // Since we used the elvis-operator to null check, we also don't need a safe call here
    val email:String = info.email ?: return
    
    mailer.sendMessage(email, message)
}

class Client (val personalInfo: PersonalInfo?)
class PersonalInfo (val email: String?)
interface Mailer {
    fun sendMessage(email: String, message: String)
}
