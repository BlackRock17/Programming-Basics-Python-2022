v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

flow_p1 = p1 * h
flow_p2 = p2 * h
total_flow = flow_p1 + flow_p2

total_flow_percent = v - (abs(total_flow - v))
total_flow_percent = total_flow_percent / v * 100

flow_p1_percent = total_flow - abs(flow_p1 - total_flow)
flow_p1_percent = flow_p1_percent / total_flow * 100

flow_p2_percent = total_flow - abs(flow_p2 - total_flow)
flow_p2_percent = flow_p2_percent / total_flow * 100

if total_flow <= v:
    print(f"The pool is {total_flow_percent:.2f}% full."
          f" Pipe 1: {flow_p1_percent:.2f}%. Pipe 2: {flow_p2_percent:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {total_flow - v:.2f} liters.")









