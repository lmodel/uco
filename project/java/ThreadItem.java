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
  A ThreadItem is a member of a thread.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ThreadItem extends UcoThing {

  private URI id;
  private UcoObject itemContent;
  private List<ThreadItem> threadNextItem;
  private List<ThreadItem> threadPredecessor;
  private List<ThreadItem> threadPreviousItem;
  private List<ThreadItem> threadSuccessor;


}