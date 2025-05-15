import { useEffect, useState } from 'react';
import { useAtom } from 'jotai';
import clsx from 'clsx';
import { ctxMain } from '../../contexts/ctxMain';

export function NotesView() {
	const [, setDB] = useAtom(ctxMain.toDos);
	const [option, setOption] = useAtom(ctxMain.optionBar);

	// Requisição de todos os dados
	useEffect(() => {
		//
		(async () => {
			let resp;
			try {
				resp = await (await fetch('http://127.0.0.1:5000/toDo/cards')).json();
			} catch (error) {
				resp = [];
				console.log(`Error: ${error}`);
			}
			setDB((prev) => [...prev, ...resp]);
		})();
		//
	}, []);

	const filterMap = () => {};

	return <div className='w-134 h-full overflow-auto'></div>;
}

interface Item {
	title: string;
	content: string;
	validity: string;
	favorited: boolean;
}

// function Note({ item }: { item: Item }) {
// 	const [DB, setDB] = useAtom(ctxMain.toDos);
// 	const [title, setTitle] = useState(item.title);
// 	const [content, setContent] = useState(item.content);
// 	const [validity, setValidity] = useState(item.validity);
// 	const [favo, setFavo] = useState(item.favorited);

// 	const Delete = (id) => {
// 		const newDB = DB.filter((item) => item.id !== id);
// 		setDB(newDB);
// 		Exchange(id, `http://127.0.0.1:5000/toDo/cards/${id}`, 'DELETE');
// 	};

// 	const Update = (id) => {
// 		// Atualizar Local DB
// 		const item = DB.map((task) => {
// 			if (task.id === id) {
// 				return {
// 					...task,
// 					title: title,
// 					content: content,
// 					favorited: favo,
// 					validity: validity,
// 				};
// 			} else {
// 				return task;
// 			}
// 		});
// 		setDB(item);

// 		// Atualizar Server DB
// 		Exchange(
// 			{ title: title, content: content, favorited: favo, validity: validity },
// 			`http://127.0.0.1:5000/toDo/cards/${id}`,
// 			'PUT'
// 		);
// 	};

// 	useEffect(() => {
// 		Update(props.item.id);
// 	}, [title, content, favo]);

// 	return (
// 		<div className='note'>
// 			<div className='formNote'>
// 				<input
// 					type='text'
// 					placeholder='Title...'
// 					value={title}
// 					onChange={(e) => {
// 						setTitle(e.target.value);
// 					}}
// 					spellCheck='false'
// 					maxLength={64}
// 				/>
// 				<textarea
// 					placeholder='Content'
// 					value={content}
// 					onChange={(e) => {
// 						setContent(e.target.value);
// 					}}
// 					spellCheck='false'
// 				/>
// 				<div className='toolsNote'>
// 					<button
// 						className='deleteNote'
// 						onClick={() => Delete(props.item.id)}>
// 						<RiDeleteBin2Line />
// 					</button>
// 					<input
// 						type='date'
// 						className='validade'
// 						value={validity}
// 						onChange={(e) => setValidity(e.target.value)}
// 						onBlur={(e) => {
// 							if (moment(e.target.value, 'YYYY-MM-DD').isValid()) {
// 								Update(props.item.id);
// 							}
// 						}}
// 						min={props.item.date}
// 					/>
// 					<button
// 						className='saveNote'
// 						onClick={() => setFavo(!favo)}>
// 						<FaCheckSquare style={{ color: favo ? '#4eff98' : '' }} />
// 					</button>
// 					<span className='trueDate'>
// 						{moment(props.item.date).format('DD MMM YYYY')}
// 					</span>
// 				</div>
// 			</div>
// 		</div>
// 	);
// }
