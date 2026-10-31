package example;

/* metamodel_version: 1.12.0 */
/* version: 1.5.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A forum post is message submitted by a user account to an online forum where the message content (and typically metadata including who posted it and when) is viewable by any party with viewing permissions on the forum.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ForumPost extends Message {



}